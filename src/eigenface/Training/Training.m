%% No average
height = 120;
width = 90;
image_size = [height, width];
pixel_num = height*width;

files = dir('Data');
num = length(files) - 2; % IGNORE root
Data = zeros(num, pixel_num);
for k=1:num % IGNORE current and parent directory . and ..
    Data(k, :) = reshape(imresize(double(rgb2gray(imread("Data\"" + files(k + 2).name))), image_size), 1, pixel_num);
end % obtain a data matrix where every row is an image

Corr = Data'*Data;
[V, D] = eigs(Corr, 20, 'lm');
%figure(1)
pcolor(flipud(reshape(V(:,2), height, width))), shading interp, colormap(gray);

Keys = Data*V;

% Test
Test = reshape(imresize(double(rgb2gray(imread("Test\" + "Arya.png"))), image_size), 1, pixel_num);
TKey = Test*V;
output_non_ave = zeros(1,num);
for k=1:num
    output_non_ave(1,k) = norm(TKey - Keys(k,:));
end
figure(3)
bar(output_non_ave)

%% Averaged

height = 120;
width = 90;
image_size = [height, width];
pixel_num = height*width;
model = reshape(imresize(rgb2gray(imread("Model_Small.png")), image_size), pixel_num, 1);

files = dir('Data');
num = length(files) - 2; % IGNORE root directory
Data = zeros(pixel_num, num);
ave_vec = zeros(pixel_num, 1);
for k=1:num % ignore current and parent directory . and ..
    image_vec = reshape(imresize(double(rgb2gray(imread("Data\" + files(k+2).name))), image_size), pixel_num, 1);
    image_vec = scoop(image_vec, model);
    ave_vec = ave_vec + image_vec;
    Data(:,k) = image_vec;
end % obtain a data matrix where every column is an image

% Average each image
ave_vec = ave_vec / num;
for k=1:num
    Data(:,k) = Data(:,k) - ave_vec;
end
%pcolor(flipud(reshape(Data(:,29), height, width))), shading interp, colormap(gray);

% Compute eigenspace V of Data
[Vf, D] = eigs(Data'*Data, 20, 'lm');
V = Data*Vf;
for k=1:20
    V(:,k) = V(:,k) / norm(V(:,k));
end
figure(1)
pcolor(flipud(reshape(V(:,1), height, width))), shading interp, colormap(gray);

Keys = Data'*V;

% Test
Test = reshape(imresize(double(rgb2gray(imread("Data\" + "zz1.png"))), image_size), pixel_num, 1) - ave_vec;
Test = scoop(Test, model);

figure(4)
subplot(1,2,1), pcolor(flipud(reshape(Test, height, width))), shading interp, colormap(gray);
subplot(1,2,2), pcolor(flipud(reshape(Data(:,33), height, width))), shading interp, colormap(gray);

TKey = Test'*V;
output_ave = zeros(1,12);
for k=1:num
    output_ave(1, k) = norm(TKey - Keys(k,:));
    % HOG/LBP + SVM
    % LeNet SIFT
end
figure(3)
bar(output_ave);

function image = scoop(image, model)
    for j=1:length(image)
        if model(j,1) <= 3
            image(j,1) = 0.0;
        end
    end
end




