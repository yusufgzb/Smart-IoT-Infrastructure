
>docker exec -it kafka-docker bash

>kafka-topics.sh --create --topic ornek --bootstrap-server localhost:9092
    
    Created topic ornek.




#Console producer

>kafka-console-producer.sh --topic newtopic2 --bootstrap-server localhost:9092

>first message
>realtime message



#console consumer realtime

>kafka-console-consumer.sh --topic newtopic2 --bootstrap-server localhost:9092
    
    first message
    realtime message
