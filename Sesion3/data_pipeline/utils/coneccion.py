

def create_db_engine(config):
    """
    Crea una conexión de motor a la base de datos MySQL.
    """
    try:
        engine = create_engine(
            f"mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}",
            echo=False
        )
        logging.info("Conexión a la base de datos establecida correctamente.")
        return engine
    except Exception as e:
        logging.error(f"Error al conectar a la base de datos: {e}")
        sys.exit(1)
