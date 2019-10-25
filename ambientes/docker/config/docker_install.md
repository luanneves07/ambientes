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

#### Fonte
Este bizu foi criado baseado nas informações contidas no fórum docs.docker.
Para acessar, clique [aqui](https://docs.docker.com/install/)