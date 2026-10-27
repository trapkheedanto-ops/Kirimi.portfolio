import re
s=open("/workspace/patchwork/stage1.py",encoding="utf-8").read()
start=s.index("EXTRA = {")
end=s.index("\ncount_inject")
region=s[start+len("EXTRA = "):end]
out=[]
for ln in region.split("\n"):
    st=ln.strip()
    if not st: out.append(ln); continue
    m=re.match(r'^(\w+):',st)
    if m and m.group(1) in ("lang","pop","history","art","traditions","economy","sources"):
        rest=st[len(m.group(0)):]
        closer=""
        if rest.endswith('"),'): val=rest[:-2]; closer='"],'   # sources line closing dict(...) ,
        elif rest.endswith('")'):  val=rest[:-2]; closer='")'
        else: val=rest
        out.append('        "%s": %s%s'%(m.group(1),val,closer))
    elif st.startswith("links=["):
        rest=st[len("links="):]
        out.append('        "links": '+rest)
    else:
        out.append(ln)
new="\n".join(out)
# fix dangling openers: 'dict(\n ... "sources": "...")' already closes with ). But we changed closers to "]," which is wrong.
# Actually sources lines end with .") meaning string then close paren of dict(. Replace those with ." ) -> keep as string + close.
s2=s[:start+len("EXTRA = ")]+new+s[end:]
open("/workspace/patchwork/stage1c.py","w",encoding="utf-8").write(s2)
print("done")
