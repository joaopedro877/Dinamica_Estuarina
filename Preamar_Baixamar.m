%%
DIF=diff(nivel_filt);
for i=2:length(DIF)
    if DIF(i-1)>0 && DIF(i+1)<0 %PREAMAR
        preamar(i)=nivel_filt(i);
        tempo_prea(i)=time_adcp(i);
    else
        preamar(i)=NaN;
        tempo_prea(i)=NaN;
    end
end

%%
DIF=diff(nivel_filt);
for i=2:length(DIF)
    if DIF(i-1)<0 && DIF(i+1)>0 %BAIXAMAR
        baixamar(i)=nivel_filt(i);
        tempo_baixa(i)=time_adcp(i);
    else
        baixamar(i)=NaN;
        tempo_baixa(i)=NaN;
    end
end

