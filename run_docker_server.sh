docker rm kaiko
docker run -d --name kaiko -p 5100:5100 -v $(pwd)/model:/app/model -v $(pwd)/mgf_input:/app/mgf_input -v $(pwd)/decode_output:/app/decode_output kaiko run_server.sh