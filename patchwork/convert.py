import re
P="/workspace/patchwork/stage1.py"
s=open(P,encoding="utf-8").read()
# find EXTRA dict region: from "EXTRA = {" to the line "}\n\ncount_inject"
start=s.index("EXTRA = {")
end=s.index("\ncount_inject")
region=s[start+len("EXTRA = "):end]
lines=region.split("\n")
out=[]
for ln in lines:
    st=ln.strip()
    if not st: out.append(ln); continue
    m=re.match(r'^(\w+):',st)
    if m and m.group(1) in ("lang","pop","history","art","traditions","economy","sources"):
        rest=st[len(m.group(0)):]
        # strip trailing comma for value, keep it outside
        if rest.endswith(","):
            val=rest[:-1]; tail=","
        else:
            val=rest; tail=""
        out.append('        "%s": %s%s'%(m.group(1),val,tail))
    elif st.startswith("links=["):
        rest=st[len("links="):]
        if rest.endswith(","): rest=rest[:-1]+","
        out.append('        "links": '+rest)
    elif re.match(r'^"[^"]+"\s*:\s*dict\($',st):
        name=st.split(":")[0]
        out.append('    %s: dict('%name)
    else:
        out.append(ln)
new_region="\n".join(out)
s2=s[:start+len("EXTRA = ")]+new_region+s[end:]
open("/workspace/patchwork/stage1b.py","w",encoding="utf-8").write(s2)
print("written stage1b.py")
