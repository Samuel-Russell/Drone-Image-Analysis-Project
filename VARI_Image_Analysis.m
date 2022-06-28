%% MATLAB GIS, GEOHAZARDS, GEORISKS FINAL PROJECT 
%%
clear, close all
%% Reading in Example 
x=imread('carpark.jpg');
size(x)
%% Reading and saving individual spectrum bands
imshow(x)
figure,imshow(x(:,:,1))
saveas(gcf,'red.png')
figure,imshow(x(:,:,2))
saveas(gcf,'green.png')
figure,imshow(x(:,:,3))
saveas(gcf,'blue.png')

%% 
RED = imread('red.png');
GREEN = imread('green.png');
BLUE = imread('blue.png');

%% Isolating individual spectrum bands
red = x(:,:,1);
green = x(:,:,2);
blue = x(:,:,3);

%% Computing VARI
VARI = (double(green) - double(red)) ./ (double(green) + double(red) - double(blue));
figure, imshow(VARI);

%% VARI Image
imagesc(VARI), axis off, colormap(winter), colorbar
caxis([-1 1]); % set colormap limits

%% Threshold determining

threshold = 0.3;
q = (VARI > threshold);
%% Caclulating Percentage
100 * numel(red(q(:))) / numel(red);

%% Showing Threshold Image
imshow(q);
title('NDVI with Threshold Applied');
