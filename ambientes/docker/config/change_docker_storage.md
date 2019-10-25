# Criando um link simbólico para gravar as imagens docker

Os passos abaixo foram baseados na [resposta](https://forums.docker.com/t/how-do-i-change-the-docker-image-installation-directory/1169) do usuário nhazlett do fórum docker

1. Parar o serviço docker:

```$ service docker stop```

2. Dentro do diretório ```/var/lib/docker/``` é onde as imagens e mais alguns arquivos referentes ao funcionamento do docker
são armazenados. (É interessante manter um backup deste diretório antes de mais nada)

```$ tar -zcC /var/lib docker > /home/var_lib_docker-backup-$(date +%s).tar.gz```

3. Mova o diretório ```/var/lib/docker/``` para o seu novo disco.

```$ mv /var/lib/docker /home/DESTINO/docker```

4. Criar o link simbólico

```$ ln -s /home/DESTINO/docker /var/lib/docker```

5. Verificar que o link simbólico foi criado sem erros:

```$ ls /var/lib/docker/```

6. Iniciar o serviço de docker novamente

```$ service docker start```

7. Inicializar os containers novamente.

Desta forma as imagens agora serão gravadas no seu novo disco.