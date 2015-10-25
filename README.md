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
<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/0001-4.png">
<img src="https://raw.githubusercontent.com/Asoul/validate-captcha/master/demo/0001-5.png">

## Ranking Steps

- Calculate Mean Error for targets
- Choose the smallest error one

## Usage

- 把 [collect-captcha](https://github.com/Asoul/collect-captcha) 抓到目錄下，或用 soft link
- 預處理和切字：`python segement.py`
- 分類：`python classify.py`

## Issues

- 轉換 10000 張圖片，共 50000 個字後，共有 46024 個字可以被切出來，成功率還蠻高的，沒被切出來的可能像是兩個黏在一起的字，目前還未處理。
- Ranking 時用的 Error function 先是試 Mean Square Error，發現有些很差，換了 Delta Error 之後感覺有好一些，只是還可以改進。
- 分類上目測成功率有些字很好，有些卻很差，也需要進一步改進。

## Reference

Thanks to [David's tutorial](https://www.youtube.com/watch?t=16&v=KESG8I9C3oA)

## TODO

1. 補上實際抓的 code
2. 上櫃的還沒做