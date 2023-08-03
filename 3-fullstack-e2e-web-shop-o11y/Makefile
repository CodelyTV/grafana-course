.PHONY: no_default website website-traffic help

no_default:
	@echo "No default target specified"
	@echo "Run 'make help' to see available targets"
	@exit 2

website: ## Initializes the Website use case demo
	@echo "Starting website demo..."
	(cd web-shop-o11y-demo && PUBLIC_APP_URL=localhost ./up.sh)
	@echo "Loading some data..."
	@sleep 10
	(cd web-shop-o11y-demo && ./setup/add_products.sh phones)

website-traffic: ## Simulates traffic to the Website use case demo
	@echo "Simulating traffic..."
	(cd web-shop-o11y-demo && ./simulate-user-traffic.sh)

help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
