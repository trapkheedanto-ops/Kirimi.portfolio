const fs=require('fs');
const h=fs.readFileSync('/workspace/Fortuna Labs/east-africa-heritage.html','utf8');
const m=h.match(/var SITES = \[([\s\S]*?)\n    \];/);
try{
  const arr=eval('['+m[1]+']');
  console.log('entries:',arr.length,'history:',arr.filter(s=>s.history).length,'links:',arr.filter(s=>s.links&&s.links.length).length,'sources:',arr.filter(s=>s.sources).length,'refs:',arr.filter(s=>s.refs).length);
}catch(e){console.log('SYNTAX ERROR:',e.message)}
