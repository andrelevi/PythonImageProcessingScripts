# PythonImageProcessingScripts

A set of image utils geared towards game development and handling of various PBR texture types.\

Last tested with `Python 3.11` on Windows.

## Example Usage

### Add Image to Alpha Channel
`./add-image-to-alpha-channel.py -rgb specular.png -a smoothness.png`

Linear to Gamma:\
`./add-image-to-alpha-channel.py -rgb specular.png -a smoothness.png --suffix smoothness --exponent_power 0.454545`

Gamma to Linear:\
`./add-image-to-alpha-channel.py -rgb specular.png -a smoothness.png --suffix smoothness  --exponent_power 2.2`

### Invert Image

Invert RGB channels:\
`python invert-image.py -i image.png -c rgb`

Invert Alpha channel:\
`python invert-image.py -i image.png -c a`

### Resize Image
`python resize-image.py -i image.png --width 2048 --height 1024`