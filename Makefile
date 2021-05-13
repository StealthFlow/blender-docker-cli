export PWD=`pwd`
export CONTAINER_NAME=blender_cli

build:
	docker build -f Dockerfile \
		-t $(CONTAINER_NAME) .

in:
	docker run -it --rm --gpus all \
	-v $(PWD):/work \
	blender_cli \
	/bin/bash

run:
	-rm -f blender/generated.blend
	docker run -it --rm --gpus all \
	-v $(PWD):/work \
	blender_cli \
	blender --background --python ./scripts/test_script.py