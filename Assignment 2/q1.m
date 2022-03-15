clear all
clc

temp=imread('propeller.png');
img = rgb2gray(temp);

disp('Apply Inverse Geometric Transformation');
disp('1. Flip vertically');
disp('2. Rotate by 45 deg');
disp('3. Shear vertically');

n = input('Enter a number: ');

switch n
    case 1
        transform(img, 1, 45);
    case 2
        transform(img, 2, 45);
    case 3
        transform(img, 3, 45);
    otherwise
        disp('input invalid')
end

function transform(img, c, theta) 

figure,imshow(img); 
title('Original Image');
[row,  col] = size(img);

% Flip vertically
if c == 1 
    for i = 1:row
        for j = 1:col
            flip(i,j) = img(i, col-j+1);
        end
    end
    figure,imshow(flip); 
    title('Flipped vertically');   
% Rotate by 45
elseif c == 2
    rads=2*pi*theta/360;  

    %calculating array dimesions such that  rotated image gets fit in it exactly.
    % we are using absolute so that we get  positve value in any case ie.,any quadrant.

    rowsf=ceil(row*abs(cos(rads))+col*abs(sin(rads)));                      
    colsf=ceil(row*abs(sin(rads))+col*abs(cos(rads)));                     

    % define an array withcalculated dimensionsand fill the array  with zeros ie.,black
    rot=uint8(zeros([rowsf colsf]));

    %calculating center of original and final image
    xo=ceil(row/2);                                                            
    yo=ceil(col/2);

    midx=ceil((size(rot,1))/2);
    midy=ceil((size(rot,2))/2);

    % in this loop we calculate corresponding coordinates of pixel of A 
    % for each pixel of C, and its intensity will be  assigned after checking
    % weather it lie in the bound of A (original image)
    for i=1:size(rot,1)
        for j=1:size(rot,2)                                                       
             x= (i-midx)*cos(rads)+(j-midy)*sin(rads);                                       
             y= -(i-midx)*sin(rads)+(j-midy)*cos(rads);                             
             x=round(x)+xo;
             y=round(y)+yo;
             
             if (x>=1 && y>=1 && x<=size(img,1) &&  y<=size(img,2) ) 
                  rot(i,j)=img(x,y);  
             end
        end
    end
    figure,imshow(rot); 
    title('Rotated by 45');
    
% Shear vertically by 45
elseif c == 3
    img = double(img);             
    
    [x, y] = meshgrid(1:row, 1:col);  
    coords = [x(:).'; y(:).'];            
    shearMatrix = [1 0.2; 0 1];           
    newCoords = shearMatrix*coords; % multiplying with the shear matrix      
    shear = interp2(img, newCoords(1, :),newCoords(2, :),'linear', 0);                   
    shear = reshape(shear, row, col);  
    shear = uint8(shear);    


    figure,imshow(shear); 
    title('Sheared vertically');   
end

end