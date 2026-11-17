import json,subprocess
W=json.load(open('vo/words.json'))
GAP={1:0.55,6:0.5,7:0.15,9:0.25,10:0.4,13:0.5,14:0.25,16:0.2,17:0.2,19:0.35,21:0.45}
t=0.4; inputs=[]; fl=[]
for k,w in enumerate(W):
    s=max(0,w['words'][0][0]-0.05); e=w['words'][-1][1]+0.18; off=t-s
    w['start']=t; w['end']=t+(e-s); w['abs']=[[a+off,b+off,x] for a,b,x in w['words']]
    inputs+=['-i',f'vo/s{k:02d}.mp3']
    fl.append(f"[{k}:a]atrim={s:.3f}:{e:.3f},asetpts=PTS-STARTPTS,aresample=48000,adelay={int(t*1000)}|{int(t*1000)}[a{k}]")
    t=w['end']+GAP.get(k,0.22)
total=t+2.2
fl.append("".join(f"[a{k}]" for k in range(len(W)))+f"amix=inputs={len(W)}:normalize=0,apad=whole_dur={total:.2f},loudnorm=I=-15:TP=-1.5[out]")
subprocess.run(['ffmpeg','-v','error','-y',*inputs,'-filter_complex',";".join(fl),'-map','[out]','-ar','48000','-ac','2','voice.wav'],check=True)
json.dump(dict(total=total,sent=W),open('timeline.json','w'),ensure_ascii=False); print("total",round(total,2))
