from enum import Enum


# From https://coppermind.net/wiki/Spheres#Value
class RosharanGemSize(Enum):
    CHIP = 1
    MARK = 5
    BROAM = 20


# From https://coppermind.net/wiki/Spheres#Value
class RosharanGemTier(Enum):
    CHEAPEST = 1
    LESS_WEIGHT = 5
    MIDDLE_WEIGHT = 10
    PRIME_PAIR = 25
    HIGHEST = 50


# From https://coppermind.net/wiki/Spheres#Value
class RosharanGemType(Enum):
    def __new__(cls, *args):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, tier: RosharanGemTier) -> None:
        self.tier = tier

    AMETHYST = RosharanGemTier.PRIME_PAIR
    DIAMOND = RosharanGemTier.CHEAPEST
    EMERALD = RosharanGemTier.HIGHEST
    GARNET = RosharanGemTier.LESS_WEIGHT
    HELIODOR = RosharanGemTier.LESS_WEIGHT
    RUBY = RosharanGemTier.MIDDLE_WEIGHT
    SAPPHIRE = RosharanGemTier.PRIME_PAIR
    SMOKESTONE = RosharanGemTier.MIDDLE_WEIGHT
    TOPAZ = RosharanGemTier.LESS_WEIGHT
    ZIRCON = RosharanGemTier.MIDDLE_WEIGHT


# From https://coppermind.net/wiki/Spheres#Value
class RosharanSphere(Enum):
    def __new__(cls, *args):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(
        self,
        gem_type: RosharanGemType,
        gem_size: RosharanGemSize,
    ) -> None:
        self.gem_type = gem_type
        self.gem_size = gem_size
        self.clearchips = gem_type.tier.value * gem_size.value

    AMETHYST_CHIP = RosharanGemType.AMETHYST, RosharanGemSize.CHIP
    AMETHYST_MARK = RosharanGemType.AMETHYST, RosharanGemSize.MARK
    AMETHYST_BROAM = RosharanGemType.AMETHYST, RosharanGemSize.BROAM

    CLEARCHIP = RosharanGemType.DIAMOND, RosharanGemSize.CHIP
    CLEARMARK = RosharanGemType.DIAMOND, RosharanGemSize.MARK
    DIAMOND_BROAM = RosharanGemType.DIAMOND, RosharanGemSize.BROAM

    EMERALD_CHIP = RosharanGemType.EMERALD, RosharanGemSize.CHIP
    EMERALD_MARK = RosharanGemType.EMERALD, RosharanGemSize.MARK
    EMERALD_BROAM = RosharanGemType.EMERALD, RosharanGemSize.BROAM

    GARNET_CHIP = RosharanGemType.GARNET, RosharanGemSize.CHIP
    GARNET_MARK = RosharanGemType.GARNET, RosharanGemSize.MARK
    GARNET_BROAM = RosharanGemType.GARNET, RosharanGemSize.BROAM

    HELIODOR_CHIP = RosharanGemType.HELIODOR, RosharanGemSize.CHIP
    HELIODOR_MARK = RosharanGemType.HELIODOR, RosharanGemSize.MARK
    HELIODOR_BROAM = RosharanGemType.HELIODOR, RosharanGemSize.BROAM

    FIRECHIP = RosharanGemType.RUBY, RosharanGemSize.CHIP
    FIREMARK = RosharanGemType.RUBY, RosharanGemSize.MARK
    RUBY_BROAM = RosharanGemType.RUBY, RosharanGemSize.BROAM

    SAPPHIRE_CHIP = RosharanGemType.SAPPHIRE, RosharanGemSize.CHIP
    SAPPHIRE_MARK = RosharanGemType.SAPPHIRE, RosharanGemSize.MARK
    SAPPHIRE_BROAM = RosharanGemType.SAPPHIRE, RosharanGemSize.BROAM

    SMOKESTONE_CHIP = RosharanGemType.SMOKESTONE, RosharanGemSize.CHIP
    SMOKESTONE_MARK = RosharanGemType.SMOKESTONE, RosharanGemSize.MARK
    SMOKESTONE_BROAM = RosharanGemType.SMOKESTONE, RosharanGemSize.BROAM

    TOPAZ_CHIP = RosharanGemType.TOPAZ, RosharanGemSize.CHIP
    TOPAZ_MARK = RosharanGemType.TOPAZ, RosharanGemSize.MARK
    TOPAZ_BROAM = RosharanGemType.TOPAZ, RosharanGemSize.BROAM

    ZIRCON_CHIP = RosharanGemType.ZIRCON, RosharanGemSize.CHIP
    ZIRCON_MARK = RosharanGemType.ZIRCON, RosharanGemSize.MARK
    ZIRCON_BROAM = RosharanGemType.ZIRCON, RosharanGemSize.BROAM
