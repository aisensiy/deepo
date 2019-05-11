python ../generator/generate.py ../openbayes-docker/Dockerfile.tensorflow-1.13.1-py36-cu100 tensorflow==1.13.1 python==3.6 opencv onnx jupyterlab spacy keras xgboost --cuda-ver 10.0 --cudnn-ver 7
python ../generator/generate.py ../openbayes-docker/Dockerfile.tensorflow-2.0.0a0-py36-cu100 tensorflow==2.0.0a0 python==3.6 opencv onnx jupyterlab spacy keras xgboost --cuda-ver 10.0 --cudnn-ver 7
python ../generator/generate.py ../openbayes-docker/Dockerfile.tensorflow-1.13.1-py36-cpu tensorflow==1.13.1 python==3.6 opencv onnx jupyterlab spacy keras xgboost
python ../generator/generate.py ../openbayes-docker/Dockerfile.tensorflow-2.0.0a0-py36-cpu tensorflow==2.0.0a0 python==3.6 opencv onnx jupyterlab spacy keras xgboost
