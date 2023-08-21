clear all
clc

img = imread('propeller.png');

rot = imread('rot.png');

figure(1), imshow(img); 
title('Original Image');
figure(2), imshow(rot);
title('Rotated Image');

img=double(img);
rot=double(rot);

imbed= 4;

%shift the message image over (8-imbed) bits to right
messageshift=bitshift(rot,-(8-imbed));

%show the message image with only embed bits on screen
%must shift from LSBs to MSBs
showmess=uint8(messageshift);
showmess=bitshift(showmess,8-imbed);
figure(3),imshow(showmess);
title('embed Image to Hide ');

%now zero out imbed bits in cover image
coverzero = img;

for i=1:imbed
coverzero=bitset(coverzero,i,0);
end

%now add message image and cover image
coverzero1=imresize(coverzero,[250,250]);
coverzero1=double(coverzero1);
hidden = uint8(img-messageshift);
figure(4),imshow(hidden);
title('Hidden image');