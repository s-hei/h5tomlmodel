import sys
import coremltools

if len(sys.argv) is not 3:
    print('Should specify 2 args, input file, output file without filename extension')
    exit()

path = sys.argv[1]
converted = sys.argv[2]

coreml_model = coremltools.converters.keras.convert(path,
input_names = 'image',
image_input_names = 'image'
)

coreml_model.save(converted + '.mlmodel')
