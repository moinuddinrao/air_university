clc
clear all
close all

a=imread('1.jfif');
b=rgb2gray(a);

subplot(2,2,1);
imshow(b);
title('Image 1');

im2 = imread('2.jpg');
subplot(2,2,2);
imshow(im2);
title('Image 2');

im1=histeq(b);
subplot(2,2,3);
imhist(im1);
title('Histogram equalization of Image 1');

M = zeros(256,1,'uint8'); %// Store mapping - Cast to uint8 to respect data type
hist1 = imhist(im1); %// Compute histograms
hist2 = imhist(im2);
cdf1 = cumsum(hist1) / numel(im1); %// Compute CDFs
cdf2 = cumsum(hist2) / numel(im2);

%// Compute the mapping
for idx = 1 : 256
    [~,ind] = min(abs(cdf1(idx) - cdf2));
    M(idx) = ind-1;
end

%// Now apply the mapping to get first image to make
%// the image look like the distribution of the second image
out = M(double(im2)+1);
subplot(2,2,4);
imshow(out);
title('Image 2 after histogram matching');