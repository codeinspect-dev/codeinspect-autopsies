"""
CodeInspect Forensic Autopsy - Episode 04
Incident: Knight Capital Group SMARS Failure (August 1, 2012)
Flaw: Manual deployment failure leaving Server #8 executing dormant 2003 code.
"""

class ProductionServer:
    def __init__(self, server_id: int, binary_version: str):
        self.server_id = server_id
        self.binary_version = binary_version
        self.total_shares_traded = 0
        self.capital_lost = 0.0

    def route_order(self, stock: str, target_shares: int, flag_repurposed: bool):
        print(f"\n[Server #{self.server_id}] Order Inflow: {stock} ({target_shares} shares)")
        
        if self.binary_version == "v2012.8.1":
            self.total_shares_traded += target_shares
            print(f"  -> Processed via New Retail Liquidity logic. Verified complete.")
            
        elif self.binary_version == "v2003.5.0" and flag_repurposed:
            print("  [CRITICAL] Repurposed flag activated dormant 2003 'Power Peg' logic!")
            print("  [DEFECT] Parent fill tracking missing on legacy binary. Runaway loop active.")
            
            for tick in range(1, 6):
                child_order = target_shares
                self.total_shares_traded += child_order
                loss = child_order * 0.15
                self.capital_lost += loss
                print(f"    [Tick {tick}] Executing child order: {child_order} shares | Loss: +${loss:,.2f}")

            print(f"  [RUNAWAY CEILING] Server #8 Total Loss: ${self.capital_lost:,.2f}")

def run_simulation():
    print("=" * 65)
    print("CODEINSPECT AUTOPSY: KNIGHT CAPITAL GROUP ($440M GLITCH)")
    print("=" * 65)

    servers = [ProductionServer(i, "v2012.8.1") for i in range(1, 8)]
    servers.append(ProductionServer(8, "v2003.5.0"))

    FLAG_ACTIVE = True

    for s in servers:
        s.route_order(stock="AAPL", target_shares=1000, flag_repurposed=FLAG_ACTIVE)

if __name__ == "__main__":
    run_simulation()
