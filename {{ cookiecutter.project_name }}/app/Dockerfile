FROM public.ecr.aws/lambda/python:{{ cookiecutter.python_version }}

LABEL MAINTAINER="{{ cookiecutter.author }}"
LABEL CONTACT="{{ cookiecutter.email }}"

# ensure libs are up to date
RUN : \
    && yum -y update --security \
    && yum clean all \
    && rm -rf /var/cache/yum \
    :

COPY app.py requirements.txt ./

RUN : \
    && python{{ cookiecutter.python_version }} -m pip install -r requirements.txt \
    &&:

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
