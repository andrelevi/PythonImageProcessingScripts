# PythonImageProcessingScripts

A set of image utils geared towards game development and handling of various PBR texture types.

Last tested with `Python 3.11` on Windows.

### Purpose
Game engines (Unity, Unreal, etc) use shaders that require a specific packed texture format. For example, Unity requires metallic data packed in the (R) channel, and smoothness packed in the (A) channel. However, some assets may only provide a roughness map, meaning you must first invert that roughness map to create a smoothness map, and then set that smoothness map as the alpha channel of a metallic map.

# Example Usage

Place images in `images/`. By default, scripts search `images/` for relative image file paths.

### Add Image to Alpha Channel
`python add-image-to-alpha-channel.py -rgb specular.png -a smoothness.png`

Linear to Gamma:\
`python add-image-to-alpha-channel.py -rgb specular.png -a smoothness.png --suffix smoothness --exponent_power 0.454545`

Gamma to Linear:\
`python add-image-to-alpha-channel.py -rgb specular.png -a smoothness.png --suffix smoothness  --exponent_power 2.2`

### Invert Image

Invert RGB channels:\
`python invert-image.py -i roughness.png -c rgb`

Invert Alpha channel:\
`python invert-image.py -i metallic_roughness.png -c a`

### Resize Image
`python resize-image.py -i image.png --width 2048 --height 1024`