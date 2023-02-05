import enum
from game.model.sqlite_template_factory import template_factory


class Attribute(enum.Enum):
    GOLD = ("gold", int, 3)
    WOOD = ("wood", int, 10)
    CRYSTAL = ("crystal", int, 0)
    GEMSTONE = ("gemstone", int, 0)

    def __init__(self, name, value_type: type, default):
        self.id = name
        self.value_type = value_type
        self.default = default

    @staticmethod
    def of(name):
        for attr in Attribute:
            if attr.id == name:
                return attr


class Player:
    __attrs = None

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def attr(self, attr_type: Attribute):
        self.__load_attrs()
        if attr_type.id not in self.__attrs:
            self.__attrs[attr_type.id] = PlayerRepository.create_attr(self.id, attr_type)
        attr = self.__attrs[attr_type.id]
        return attr_type.value_type(self.__attrs[attr.name].value)

    def set_attr(self, attr_type_for_update: Attribute, new_value):
        updating_attr = self.__attrs[attr_type_for_update.id]
        PlayerRepository.update_attr(
            updating_attr.id,
            new_value
        )
        updating_attr.value = new_value

    def attrs(self):
        self.__load_attrs()
        return self.__attrs

    def __load_attrs(self):
        if not self.__attrs:
            self.__attrs = PlayerRepository.player_attrs(self.id)


class PlayerAttribute:
    def __init__(self, id, name, value):
        self.id = id
        self.name = name
        self.value = value


class PlayerRepository:
    @staticmethod
    def find_or_create(ext_id, name):
        existing_player = PlayerRepository.find(ext_id)
        if not existing_player:
            db = template_factory.new()
            new_player_id = db.execute("INSERT INTO player (ext_id, name) VALUES (?, ?)", (ext_id, name))
            db.commit()
            db.close()
            existing_player = Player(new_player_id, name)
        return existing_player

    @staticmethod
    def find(ext_id):
        db = template_factory.new()
        row = db.select_one("SELECT id, name FROM player WHERE ext_id = ?", (str(ext_id)))
        db.close()
        return Player(row[0], row[1]) if row else None

    @staticmethod
    def player_attrs(player_id):
        db = template_factory.new()
        rows = db.select(
            """
            SELECT pav.id, pa.name, pav.value 
            FROM player_attr_value pav
            JOIN player_attr pa ON pa.id = pav.attr_id
            WHERE pav.player_id = ?
            """,
            player_id
        )
        db.close()
        return dict((row[1], PlayerAttribute(row[0], row[1], row[2])) for row in rows)

    @staticmethod
    def all_attrs():
        db = template_factory.new()
        rows = db.select("SELECT id, name FROM player_attr")
        db.close()
        return dict((row[0], PlayerAttribute(row[0], row[1], row[2])) for row in rows)

    @staticmethod
    def update_attr(attr_id, new_value):
        db = template_factory.new()
        db.execute(
            """
            UPDATE player_attr_value
            SET value = ?
            WHERE id = ?
            """,
            (new_value, attr_id,)
        )
        db.commit()
        db.close()

    @staticmethod
    def create_attr(player_id, attr_type: Attribute):
        db = template_factory.new()
        attr_id = db.select_value("SELECT id FROM player_attr WHERE name = ?", attr_type.id)
        player_attr_id = db.execute(
            """
            INSERT INTO player_attr_value (player_id, attr_id, value)
            VALUES (?, ?, ?)
            """,
            [player_id, attr_id, attr_type.default]
        )
        db.commit()
        db.close()
        return PlayerAttribute(player_attr_id, attr_type.id, attr_type.default)
