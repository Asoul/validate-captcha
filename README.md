# Validate Captcha from Taiwan Stock

This project is based on [collect-captcha](https://github.com/Asoul/collect-captcha)'s 10000 images. And due to solve the captcha problem from taiwan stock official website.

## Image Process Steps

### Original

<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/original.png">

### Erode

<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/erosion.png">

### Blur

<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/blurred.png">

### Edge

<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/edged.png">

### Dilate

<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/dilation.png">

### Segment and Resize

<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/0001-0.png">
<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/0001-1.png">
<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/0001-2.png">
<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/0001-4.png">
<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/0001-5.png">

## Ranking Steps

- Calculate Mean Error for targets
- Choose the smallest error one

## Usage

- 把 [collect-captcha](https://github.com/Asoul/collect-captcha) 抓到目錄下，或用 soft link
- 預處理和切字：`python segement.py`
- 分類：`python classify.py`

## Reference

Thanks to [David's tutorial](https://www.youtube.com/watch?t=16&v=KESG8I9C3oA)
