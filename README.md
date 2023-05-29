# exemplo-coleta-de-dados

Este repositório contém o código para exemplo de criação de uma página para coleta de dados de cadastro usando **Flask** e **Bootstrap**. A página deve coletar Nome, E-mail, Telefone e CPF com as seguintes validações:

1. Os campos **Nome** e **Sobrenome** não devem possuir números.
    - VÁLIDO: Jean
    - INVÁLIDO: 1Marcos
	
2. O campo **CPF** deve possuir apenas 11 (onze) números.
    - VÁLIDO: 11122233344
    - INVÁLIDO: 865521

3. O campo **E-mail** deve seguir a estrutura: subdomínio + @ + domínio.
    - VÁLIDO: subdominio@dominio.com
    - INVÁLIDO: @dja.asd@com

4. O campo **Telefone** deve possuir DDD e números.
    - VÁLIDO: 61978524115
    - INVÁLIDO: 654321

Após a validação, é preciso apresentar uma mensagem de sucesso ou erro. Os dados coletados devem ser salvos em um arquivo do tipo CSV.

## Ambiente de desenvolvimento

1. Crie o ambiente

```bash
python -m venv pECD
```

2. Ative o ambiente

    - Em Windows (bash do git)
    ```bash
    source pECD/Scripts/activate
    ```
    
    - Em Linux
    ```bash
    source pECD/bin/activate
    ```

3. Instale as dependências

```bash
pip install -r requirements.txt
```

## Como usar

```bash
(pECD)$ python main.py 
```
