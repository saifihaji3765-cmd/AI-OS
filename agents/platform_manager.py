from config import PLATFORMS


def get_enabled_platforms():
    """
    Return active platforms
    """

    return PLATFORMS


def platform_status():
    """
    Show platform status
    """

    report = []

    for platform in PLATFORMS:

        report.append(
            f"✅ {platform} enabled"
        )

    return "\n".join(report)


def is_platform_enabled(name):
    """
    Check platform availability
    """

    return name.lower() in PLATFORMS
