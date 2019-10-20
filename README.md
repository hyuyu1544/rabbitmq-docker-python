# rabbitmq-docker-python

The purpose of this branch is to refactor the code so that the program can be reused and easily called.



# Deploy rabbitmq with docker.

First pull rabbitmq in docker:

	docker pull rabbitmq:management
	
Then run rabbitmq in docker:

	docker run -d -p 5672:5672 -p 15672:15672  —name rabbitmq rabbitmq:management


# connect rabbitmq on python

Before you connect rabbitmq on python, please install pika first:

	pip install pika

Then you can open two terminal to send and receive messages.
On first terminal:

	python receive.py
	
And you can send message in second terminal:

	python send.py
	
Refactored code in the connect_rabbitmq.py, please check.

When you send the message to rabbitmq, you also can check it on rabbitmq:

	docker exec -it [container id] bash
	rabbitmqctl list_queues
	
If you don’t sure container id, please type:

	docker ps -a
