# Validate Captcha from Taiwan Stock

This project is based on [collect-captcha](https://github.com/Asoul/collect-captcha)'s 10000 images. And due to solve the captcha problem from taiwan stock official website.

## Image Process Steps

### Original

<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/original.png">

### Erode

<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/blurred.png">

### Blur

<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/blurred.png">

### Edge

<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/edged.png">

### Dilation

<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/dilation.png">

### Segment and Resize

<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/0001-0.png">
<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/0001-1.png">
<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/0001-2.png">
<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/0001-3.png">
<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/0001-4.png">

## Ranking Steps

- calculate Mean Square Error for targets
- choose the smallest error one

## Reference

Thanks to [David's tutorial](https://www.youtube.com/watch?t=16&v=KESG8I9C3oA)

## TODO

1. 補上實際抓的 code