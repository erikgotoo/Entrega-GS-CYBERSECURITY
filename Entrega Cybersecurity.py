
from cryptography.fernet import Fernet

# Cria uma chave de segurança
chave_seguranca = Fernet.generate_key()
cipher_suite = Fernet(chave_seguranca)

# 2. Dados confidenciais
dados_originais = "-23.5631, -46.6543 (Alvo Crítico: Infestação Detectada)"
print("1. DADOS ORIGINAIS NO DISPOSITIVO DE CAMPO (DRONE):")
print(f"   {dados_originais}\n")
print("=" * 70 + "\n")

# 3. Processo de criptografia
dados_em_bytes = dados_originais.encode('utf-8')
dados_criptografados = cipher_suite.encrypt(dados_em_bytes)

print("2. PAYLOAD BLINDADO/CRIPTOGRAFADO (Pronto para o Banco de Dados):")
print(f"   {dados_criptografados}\n")
print("=" * 70 + "\n")

# 4. Processo de descriptografia
dados_decifrados_bytes = cipher_suite.decrypt(dados_criptografados)
dados_recuperados = dados_decifrados_bytes.decode('utf-8')

print("3. DADOS RECUPERADOS COM SUCESSO NO BACKEND DA SPACE CODE:")
print(f"   {dados_recuperados}")