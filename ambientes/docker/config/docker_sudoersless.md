# Utilizar docker sem chamar ```sudo```

Para se inserir dentro do grupo gerenciado pelo docker, basta seguir os passos descritos:

1. Criar o grupo docker

```$ sudo groupadd docker```

2. Adicionar-se ao grupo

```$ sudo usermod -aG docker $USER```

3. Consistir mudanças no grupo

```$ newgrp docker```

4. Executar o teste

```$ docker run hello-world```

### Inicializar docker sempre no boot (Opcional)

Basta executar o seguinte comando:

```$ sudo systemctl enable docker```

#### Fonte
Este bizu foi criado baseado nas informações contidas no fórum docs.docker.
Para acessar, clique [aqui](https://docs.docker.com/install/)