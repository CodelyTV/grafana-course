.PHONY: no_default demo help

no_default:
	@echo "No default target specified"
	@echo "Run 'make help' to see available targets"
	@exit 2

demo: ## Initializes the Grafana Scenes demo application
	@echo "Installing dependencies..."
	(cd scenes && yarn install)
	@echo "Building demo application..."
	(cd scenes && ./scripts/demo.sh)

help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
