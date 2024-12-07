import boto3
import streamlit as st

# Configurar cliente do Amazon Bedrock
def configurar_bedrock():
    return boto3.client(
        "bedrock",  # Certifique-se de que o serviço correto é utilizado
        region_name="us-east-1",  # Substitua pela sua região
    )

# Função para gerar resposta do modelo Claude
def gerar_recomendacao(client, preferencia_usuario):
    try:
        # Tente uma outra maneira de interagir com o modelo, por exemplo, usando 'invoke_endpoint' ou outro método
        response = client.invoke_endpoint(
            EndpointName="nome_do_endpoint",  # Endpoint correto para o modelo, se disponível
            Body=preferencia_usuario,
            ContentType="application/json",
            Accept="application/json",
        )
        return response["Body"].read().decode("utf-8")
    except Exception as e:
        return f"Erro ao conectar ao Amazon Bedrock: {e}"

# Interface do Streamlit
def main():
    st.title("Assistente Inteligente de Refeições Saudáveis 🍴")
    st.sidebar.header("Preferências do Usuário")

    # Inputs do usuário
    tipo_refeicao = st.sidebar.selectbox("Escolha o tipo de refeição", ["Café da Manhã", "Almoço", "Jantar", "Lanche"])
    vegano = st.sidebar.checkbox("Mostrar apenas opções veganas")
    max_calorias = st.sidebar.slider("Máximo de calorias", 100, 1000, 500)

    # Mensagem personalizada para o modelo
    preferencia_usuario = f"""
    Por favor, sugira uma refeição saudável para {tipo_refeicao}.
    Prefiro opções com até {max_calorias} calorias. { "Somente vegano." if vegano else "" }
    """

    # Gerar recomendação
    if st.sidebar.button("Gerar Refeição"):
        st.write("Gerando sua recomendação... Aguarde.")
        client = configurar_bedrock()
        resposta = gerar_recomendacao(client, preferencia_usuario)
        st.subheader("Recomendação de Refeição")
        st.write(resposta)

    # Rodapé
    st.caption("Desenvolvido por Mayra e equipe.")

if __name__ == "__main__":
    main()
