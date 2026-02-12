from src.portal_localiza import PortalLocaliza


def main():
    robo = PortalLocaliza()
    robo.iniciar_navegador()
    robo.acessar_portal()
    robo.fazer_login()

    input("Pressione ENTER para fechar...")
    robo.fechar()


if __name__ == "__main__":
    main()
