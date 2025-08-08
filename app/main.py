# app/main.py
import os

from workflows.launch_orchestrator import run_launch_orchestration
from workflows.shopify_sync import sync_shopify_products
from workflows.youtube_sync import sync_youtube_automation
from workflows.fiverr_sync import sync_fiverr_profile
from workflows.affiliate_blaster import blast_affiliate_links
from workflows.gig_replicator import replicate_gigs
from lazy_income.dropship_mirror import mirror_products
from lazy_income.content_bundle_auto import generate_bundles


def run_commander():
    print("🚀 Commander Engine Activated!")
    # Run the new orchestrator for full business automation
    run_launch_orchestration()
    # Optionally, run legacy flows for backward compatibility
    print("\n(Individual modules running for backward compatibility)")
    sync_shopify_products()
    sync_youtube_automation()
    sync_fiverr_profile()
    blast_affiliate_links()
    replicate_gigs()
    mirror_products()
    generate_bundles()
    print("✅ All systems synced.")

if __name__ == "__main__":
    run_commander()