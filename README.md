# Docker
Repositorio criado com o objetivo de manter configurações utilizados para produtividade no ambiente de desenvolvimento

Enfrentei alguns problemas para instalação do docker no linux mint 19.1 e 19.2 e resolvi centralizar aqui (Com referências) pontos que
me ajudaram a realizar a configuração.
Segue.



# Como instalar o Docker no mint 19

## Instalação

1. Primeiramente devemos garantir que o mesmo não está instalado:

```$ sudo apt-get remove docker docker-engine docker.io containerd runc```

2. Atualizar apt

```$ sudo apt-get update```

3. Instalar pacote de HTTPS no apt

```$ sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common```

4. Instalar GPG-Key

```$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -```

5. Instalar pacote do docker respectivo para o mint (bionic release)

```$ sudo add repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"```

**Obs.:** Caso esteja na versão 19.2, o instalador de pacotes foi alterado e não permite este tipo de intalação. 
Para contornar, inserir diretamente o repositório:

```$ echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable" >> /etc/apt/sources.list.d/additional-repositories.list ```

6. Atualizar apt novamente

```$ sudo apt-get update```

7. Instalar última versão do docker engine e container

```$ sudo apt-get install docker-ce docker-ce-cli containerd.io```

8. Executar teste

```$ sudo docker run hello-world```

## Inserir-se dentro do grupo docker para executar containers e docker run

1. Criar o grupo docker

```$ sudo groupadd docker```

2. Adicionar-se ao grupo

```$ sudo usermod -aG docker $USER```

3. Consistir mudanças no grupo

```$ newgrp docker```

4. Executar o teste

``` docker run hello-world```

## Inicializar docker sempre no boot

Basta executar o seguinte comando:

```$ sudo systemctl enable docker```

# Alterando storage das imagens para poupar o disco principal

Se você, assim como eu possui um disco principal e um disco secundário, é possível poupar o disco principal de armazenar
as imagens baixadas pelo docker durante o desenvolvimento.
Para isto, vou assumir que seu disco secundário apenas está inserido e não possui nem ao menos uma partição.

## Configurando o disco (Opcional)
#### O passo abaixo vai apagar todo o armazenamento em seu disco, tome cuidado

O descritivo abaixo foi baseado na [resposta](https://askubuntu.com/questions/154180/how-to-mount-a-new-drive-on-startup) dos usuários ```0x7c0``` e ```Android Dev```
do fórum askUbuntu. 

1. Executar o comando ```$ lsblk``` para identificar onde está o seu disco.

2. Executar fdisk no seu disco:

```$ sudo fdisk /dev/sdX```

3. Dentro do prompt, executar os seguintes comandos:

    3.1 Pressionar ```o``` e Enter -> Cria uma nova tabela

    3.2 Pressionar ```N``` e Enter -> Cria uma nova partição

    3.3 Pressionar ```P``` e Enter  -> Cria partição a primária

    3.4 Pressionar ```1``` e Enter -> Faz desta a primeira partição (Pode manter os tamanhos no valor default, ou alterar conforme necessidade)

    3.5 Pressionar ```W``` e Enter -> Persiste alterações no disco

4. Configurar o sistema de arquivos

```$ Run sudo mkfs.ext4 /dev/sdX1```

5. Adicionar ao fstab:

    5.1 Verificar ```UUID``` do disco para referenciar no fstab:

    ```$ blkid /dev/sda1```

    5.2 Utilizar o UUID no fstab e permitir escrita e leitura do seu usuario
    > ```$ sudo vim /etc/fstab```

    > ```UUID="INSERIR AQUI O UUID"     /CAMINHO_DE_MONTAGEM     ext4    defaults,user   0       PARTIÇÃO```

    > Salvar e sair

## Criando link simbólico

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
