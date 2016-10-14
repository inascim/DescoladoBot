function [z]=teste(b,a)

	filt(b,a)
	 
	[H,W] = freqz(b,a);
	 
	h = figure; 
	set(h,'Units','Normalized','OuterPosition',[0 0 1 1])
	
	title('FOTO');
	subplot(2,1,1);plot(W/pi,abs(H));
	ylabel('Magnitude');
	xlabel('Frequência Normalizada')
	subplot(2,1,2);plot(W/pi,phase(H));
	ylabel('Fase');
	xlabel('Frequencia Normalizada')
	print('FOTO','-dpng','-r0')
	
	z = 0;
end