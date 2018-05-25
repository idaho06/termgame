import logging
from res import config
import sqlite3

try:
    logging.debug("Session already created is: %s", __session__)
except NameError:
    __session__ = 1
    logging.debug("Session created.")

logging.info("Opening connection to database %s", config.database_file)
conn = sqlite3.connect(config.database_file)
is_ddbb_open = True

c = conn.cursor()
logging.debug("cursor created is %s", c)

c.execute('CREATE TABLE IF NOT EXISTS `termgame_version` (`major` INTEGER,`minor` INTEGER);')
conn.commit()

logging.info("Checking entries in table `termgame_version`")
c.execute('SELECT COUNT(*) FROM `termgame_version`;')
(entries_in_table_version,) = c.fetchone()
logging.info("Number of entries in lists of versions is %s", entries_in_table_version)

if entries_in_table_version == 0:
    logging.warning("No data in table `termgame_version`. Creating version %s.%s", config.database_version_major,
                    config.database_version_minor)
    c.execute(
        "INSERT INTO `termgame_version`(`major`, `minor`) VALUES ({major}, {minor});".format(
            major=config.database_version_major,
            minor=config.database_version_minor))
    conn.commit()
    logging.warning("We assume ddbb is new, so we create all needed tables here.")
    # TODO: create all needed tables

elif entries_in_table_version == 1:
    logging.info("One entry found in table `termgame_version`.")
    c.execute("SELECT `major`, `minor` FROM `termgame_version`;")
    ddbb_version_major, ddbb_version_minor = c.fetchone()
    logging.debug("Version found in `termgame_version`: %s.%s", ddbb_version_major, ddbb_version_minor)
    if eval("{}.{}".format(ddbb_version_major, ddbb_version_minor)) != eval(
            "{}.{}".format(config.database_version_major, config.database_version_minor)):
        raise Exception(
            "Database version is not supported. Version found is {db_major}.{db_minor}. Version expected is {conf_major}.{conf_minor}".format(
                db_major=ddbb_version_major, db_minor=ddbb_version_minor, conf_major=config.database_version_major,
                conf_minor=config.database_version_minor))
elif entries_in_table_version > 1:
    raise Exception(
        "More than one entry found in table `termgame_version`. Database corrupt?"
    )

conn.close()
is_ddbb_open = False
