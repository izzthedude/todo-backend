import time
from typing import Any

from django.core.management.base import BaseCommand, CommandParser
from django.db.utils import OperationalError as DjOperationError
from psycopg2 import OperationalError as PGOperationError


class Command(BaseCommand):
    help = "Attempt to connect to database and retry"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--limit",
            "-l",
            type=int,
            default=5,
            help="The maximum number of attempts",
        )

    def handle(self, *args: Any, **options: Any) -> None:
        limit: int = options.get("limit")  # type: ignore
        is_up = False

        while limit and not is_up:
            try:
                self.check(databases=["default"])
                is_up = True
                self.stdout.write(
                    self.style.SUCCESS("Successfully connected to the database")
                )
                return

            except (PGOperationError, DjOperationError):
                limit -= 1
                self.stdout.write(
                    self.style.WARNING(
                        "Database unavailable. "
                        f"Retrying {limit} more time{"" if limit == 1 else "s"}..."
                    )
                )
                time.sleep(2)

            self.stdout.write(self.style.ERROR("Failed to connect to the database"))
