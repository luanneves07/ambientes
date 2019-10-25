# Criando um disco para armazenar as imagens do Docker

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

```$ sudo mkfs.ext4 /dev/sdX1```

5. Adicionar ao fstab:

    5.1 Verificar ```UUID``` do disco para referenciar no fstab:

    ```$ blkid /dev/sda1```

    5.2 Utilizar o UUID no fstab e permitir escrita e leitura do seu usuario
    ```$ sudo vim /etc/fstab```

    ```UUID="INSERIR AQUI O UUID"     /CAMINHO_DE_MONTAGEM     ext4    defaults,user   0       PARTIÇÃO```

    > Salvar e sair