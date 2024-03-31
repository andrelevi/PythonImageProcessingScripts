# PythonImageProcessingScripts

## Python Version

Last tested with Python 3.11

## Example Usage
`./add-image-to-alpha-channel.py -rgb source.png -a smoothness.png`

Linear to Gamma
`./add-image-to-alpha-channel.py -rgb source.png -a smoothness.png --suffix smoothness --exponent_power 0.454545`

Gamma to Linear
`./add-image-to-alpha-channel.py -rgb source.png -a smoothness.png --suffix smoothness  --exponent_power 2.2`
