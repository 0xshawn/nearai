FROM public.ecr.aws/lambda/python:3.11

RUN yum install -y gcc libffi-devel openssl-devel

# pass with --build-arg FRAMEWORK=-langgraph
ARG FRAMEWORK=""

COPY nearai/aws_runner/frameworks/requirements${FRAMEWORK}.txt ${LAMBDA_TASK_ROOT}

RUN pip install -r requirements${FRAMEWORK}.txt

RUN mkdir ${LAMBDA_TASK_ROOT}/nearai
COPY nearai ${LAMBDA_TASK_ROOT}/nearai
CMD [ "nearai/aws_runner/service.handler" ]