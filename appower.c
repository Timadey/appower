#include <stdio.h>
#include <raplcap.h>

int main()
{
    raplcap handle;
    // raplcap_zone zones;
    int status;
    uint32_t num_packages;
    uint32_t num_die;

    // Initialize the RAPL library
    status = raplcap_init(&handle);
    if (status != 0)
    {
        // An error has occured exit
        fprintf(stderr, "Failed to initialize RAPL library");
        // raplcap_destroy(&handle);
        return 1;
    }

    // Get the number of available RAPL packages or processors
    num_packages = raplcap_get_num_packages(&handle);
    if (num_packages == 0)
    {
        //  An error has occured
        fprintf(stderr, "Failed to get the number of packages");
        raplcap_destroy(&handle);
        return 1;
    }

    // Get the number of die in a package
    num_die = raplcap_get_num_die(&handle, 0);
    if (num_die == 0)
    {
        //  An error has occured
        fprintf(stderr, "Failed to get the number of die");
        raplcap_destroy(&handle);
        return 1;
    }
    printf("Number of die in %u packages: %u dies", num_die, num_packages);

    if (!raplcap_pd_is_zone_supported(&handle, 0, 0, RAPLCAP_ZONE_PACKAGE))
    {
        fprintf(stderr, "RAPL Package zone not supported\n");
        raplcap_destroy(&handle);
        return 1;
    }

    if (!raplcap_pd_is_zone_enabled(&handle, 0, 0, RAPLCAP_ZONE_PACKAGE))
    {
        fprintf(stderr, "RAPL Package zone not enabled\n");
        raplcap_destroy(&handle);
        return 1;
    }

    double energy_consumed = raplcap_pd_get_energy_counter(&handle, 0, 0, RAPLCAP_ZONE_PACKAGE);
    if (energy_consumed < 0)
    {
        fprintf(stderr, "Failed to get energy consumption\n");
        raplcap_destroy(&handle);
        return 1;
    }

    printf("Energy consumed by RAPL Package: %f Joules\n", energy_consumed);

    raplcap_destroy(&handle);
    return 0;
}