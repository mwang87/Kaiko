docker rm kaiko
docker run -it --name kaiko -p 5100:5100 -v $(pwd)/model:/app/model -v $(pwd)/mgf_input:/app/mgf_input -v $(pwd)/decode_output:/app/decode_output kaiko bash
