#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <pthread.h>
#include <signal.h>
#include <string.h>
#include <time.h>
#include <math.h>

#define CPU_TARGET 39.0
#define RAM_TARGET 0.12
#define INTERVAL_MS 100

static void *memory = NULL;
static size_t allocated = 0;

static inline double now_ms(void)
{
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return ts.tv_sec * 1000.0 + ts.tv_nsec / 1000000.0;
}

size_t get_available_ram(void)
{
    FILE *f = fopen("/proc/meminfo", "r");
    if (!f)
        return 0;

    char key[64], unit[32];
    size_t value;

    while (fscanf(f, "%63s %zu %31s", key, &value, unit) == 3)
    {
        if (strcmp(key, "MemAvailable:") == 0)
        {
            fclose(f);
            return value * 1024ULL;
        }
    }

    fclose(f);
    return 0;
}

void *cpu_worker(void *arg)
{
    (void)arg;

    const double busy_ms = INTERVAL_MS * CPU_TARGET / 100.0;

    while (1)
    {
        double start = now_ms();

        while ((now_ms() - start) < busy_ms)
        {
            volatile double x = 0.0;

            for (int i = 1; i < 100000; i++)
                x += sqrt((double)i) * sin((double)i);
        }

        double elapsed = now_ms() - start;

        if (elapsed < INTERVAL_MS)
        {
            struct timespec ts;
            ts.tv_sec = 0;
            ts.tv_nsec = (long)((INTERVAL_MS - elapsed) * 1000000.0);
            nanosleep(&ts, NULL);
        }
    }

    return NULL;
}

void cleanup(int sig)
{
    (void)sig;

    if (memory)
        free(memory);

    exit(0);
}

int main(void)
{
    signal(SIGINT, cleanup);
    signal(SIGTERM, cleanup);

    size_t available = get_available_ram();

    if (available)
    {
        allocated = (size_t)(available * RAM_TARGET);


        memory = malloc(allocated);

        if (memory)
        {
            long page = sysconf(_SC_PAGESIZE);

            for (size_t i = 0; i < allocated; i += page)
                ((char *)memory)[i] = 1;
        }
        else
        {
            puts("Eror.");
        }
    }

    int cores = sysconf(_SC_NPROCESSORS_ONLN);

    pthread_t *threads = malloc(sizeof(pthread_t) * cores);

    for (int i = 0; i < cores; i++)
        pthread_create(&threads[i], NULL, cpu_worker, NULL);

    for (int i = 0; i < cores; i++)
        pthread_join(threads[i], NULL);

    free(threads);
    return 0;
}