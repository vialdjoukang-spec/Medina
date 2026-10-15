async function serve(q) {
 const repo="vialdjoukang-spec/Medina";
 function checked(r){if(r.isError)throw Error(JSON.stringify(r.structuredContent));return r.structuredContent}
 function parse(r){const x=checked(r);return JSON.parse(x.content)}
 async function head(b){let r=await tools.mcp__codex_apps__github_fetch({url:"https://api.github.com/repos/"+repo+"/git/ref/heads/"+b});if(r.isError&&r.structuredContent?.error_code==="NOT_FOUND")return null;return parse(r).object.sha}
 if(q.action==="head")return await head(q.branch);
 if(q.action==="state"){const sha=await head(q.branch);if(!sha)return {sha:null,state:{schema_version:1,closed:[],batch:0,phase:"IDLE",workers:[]}};return {sha,state:JSON.parse(checked(await tools.mcp__codex_apps__github_fetch_file({repository_full_name:repo,path:"state.json",ref:sha})).content)}}
 if(q.action==='api'){
 const prefix='repos/'+repo+'/';
 if(typeof q.path!=='string'||!q.path.startsWith(prefix)||!/^actions\/runs\/[0-9]+$/.test(q.path.slice(prefix.length)))throw Error('Read scope denied');
 return parse(await tools.mcp__codex_apps__github_fetch({url:'https://api.github.com/'+q.path}));
 }
 if(q.action==='pr'){
 if(!Number.isSafeInteger(q.number)||q.number<1)throw Error('Invalid PR number');
 const p=parse(await tools.mcp__codex_apps__github_fetch({url:'https://api.github.com/repos/'+repo+'/pulls/'+q.number}));
 if(p.base?.repo?.full_name!==repo||p.head?.repo?.full_name!==repo)throw Error('PR repository mismatch');
 const sha=p.head.sha;if(!/^[0-9a-f]{40}$/.test(sha))throw Error('Invalid PR head');
 async function pages(kind,key){let out=[],total=null;for(let page=1;page<=100;page++){
 const tail=kind==='check-runs'?'&filter=latest':'';
 const value=parse(await tools.mcp__codex_apps__github_fetch({url:'https://api.github.com/repos/'+repo+'/commits/'+sha+'/'+kind+'?per_page=100&page='+page+tail}));
 if(!Array.isArray(value[key])||!Number.isInteger(value.total_count)||value.total_count<0)throw Error('Invalid checks response');
 if(total!==null&&total!==value.total_count)throw Error('Checks changed during paginated snapshot');total=value.total_count;
 out.push(...value[key]);if(out.length>=total)return out;if(value[key].length===0)throw Error('Truncated checks snapshot');
 }throw Error('Checks pagination limit');}
 const settled=await Promise.allSettled([pages('check-runs','check_runs'),pages('status','statuses')]);
 for(const r of settled)if(r.status!=='fulfilled')throw r.reason;
 const runs=settled[0].value,contexts=settled[1].value;
 return {state:p.merged?'MERGED':String(p.state).toUpperCase(),baseRefName:p.base.ref,mergeCommit:{oid:p.merge_commit_sha},statusCheckRollup:[...runs.map(c=>({status:String(c.status).toUpperCase(),conclusion:c.conclusion===null?null:String(c.conclusion).toUpperCase()})),...contexts.map(c=>({state:String(c.state).toUpperCase()}))]};
 }
 if(q.action==="cas"){
 const allowed={"medina/7-starter-codex":"state.json","medina/session-registry":"registry.json"};
 if(allowed[q.branch]!==q.path)throw Error("Write scope denied");
 const value=JSON.parse(q.content);if(value.schema_version!==1)throw Error("Schema denied");
 let actual=await head(q.branch);if(actual!==q.expected)throw Error("CAS head mismatch");
 if(q.branch==="medina/session-registry"&&!actual)throw Error("Registry must exist");
 let trustedTree=null;
 if(q.branch==="medina/session-registry"){
 trustedTree=parse(await tools.mcp__codex_apps__github_fetch({url:"https://api.github.com/repos/"+repo+"/git/commits/"+actual})).tree.sha;
 if(q.base_tree!==trustedTree)throw Error("Registry tree mismatch");
 }else if(q.base_tree!==null)throw Error("State tree must be empty");
 let parent=q.expected;
 if(!parent){parent=await head("main");checked(await tools.mcp__codex_apps__github_create_branch({repository_full_name:repo,branch_name:q.branch,sha:parent}));}
 const blob=checked(await tools.mcp__codex_apps__github_create_blob({repository_full_name:repo,content:q.content,encoding:"utf-8"}));
 const tree=checked(await tools.mcp__codex_apps__github_create_tree({repository_full_name:repo,base_tree_sha:trustedTree,tree_elements:[{path:q.path,mode:"100644",type:"blob",sha:blob.sha}]}));
 const commit=checked(await tools.mcp__codex_apps__github_create_commit({repository_full_name:repo,parent_sha:parent,tree_sha:tree.sha,message:q.message}));
 const sha=commit.sha||commit.commit?.sha;
 checked(await tools.mcp__codex_apps__github_update_ref({repository_full_name:repo,branch_name:q.branch,expected_sha:parent,sha,force:false}));
 return parse(await tools.mcp__codex_apps__github_fetch({url:"https://api.github.com/repos/"+repo+"/git/commits/"+sha}));
 }
 throw Error("Unknown request");
}
