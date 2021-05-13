FROM nytimes/blender:2.92-cpu-ubuntu18.04

RUN mkdir /work
WORKDIR /work
CMD ["/bin/bash"]