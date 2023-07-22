#include <stdio.h>
#include <raplcap.h>

int main() {
    raplcap rc;
    int ret;

    // Initialize the RAPL library
    ret = raplcap_init(&rc);
    if (ret != 0) {
        fprintf(stderr, "Failed to initialize RAPL library: \n");
        return 1;
    }

    // Get the number of available RAPL packages
    // uint32_t num_packages;
    ret = raplcap_get_num_packages(&rc);
    if (ret == 0) {
        fprintf(stderr, "Failed to get the number of RAPL packages: \n");
        raplcap_destroy(&rc);
        return 1;
    }

    printf("Number of RAPL packages: %u\n", ret);

    // Read and print power consumption for each package
    // for (uint32_t package_id = 0; package_id < num_packages; ++package_id) {
    //     raplcap_zone domain;
    //     ret = raplcap_get_domain(rc, RAPLCAP_ZONE_PACKAGE, package_id, &domain);
    //     if (ret != 0) {
    //         fprintf(stderr, "Failed to get RAPL domain for package %u: %s\n", package_id, raplcap_error_string(ret));
    //         continue;
    //     }

    //     double power;
    //     ret = raplcap_get_power_uw(domain, &power);
    //     if (ret != 0) {
    //         fprintf(stderr, "Failed to get power consumption for package %u: %s\n", package_id, raplcap_error_string(ret));
    //         continue;
    //     }

    //     printf("Package %u Power Consumption: %.2f watts\n", package_id, power / 1.0e6); // Convert from uW to W
    // }

    // Cleanup and destroy the RAPL library context
    raplcap_destroy(&rc);

    return 0;
}
