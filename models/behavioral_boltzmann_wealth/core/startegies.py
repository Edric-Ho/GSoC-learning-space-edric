class TransferStrategy:
    def decide_transfer(self, self_wealth: int, partner_wealth: int) -> int:
        return 1 if self_wealth > 0 else 0
