import { useParams } from 'next/navigation';
import { useMemo, useState } from 'react';
import { type z } from 'zod';

import { type listRegistry } from '~/lib/models';
import { type RegistryCategory } from '~/server/api/routers/hub';
import { api } from '~/trpc/react';

import { useDebouncedValue } from './debounce';

export function useResourceParams() {
  const { namespace, name, version } = useParams();

  return {
    namespace: namespace as string,
    name: name as string,
    version: version as string,
  };
}

export function useCurrentResource(category: RegistryCategory) {
  const { namespace, name, version } = useResourceParams();

  const list = api.hub.listRegistry.useQuery({
    category,
    namespace,
    showLatestVersion: false,
  });

  const currentVersions = list.data?.filter((item) => item.name === name);

  const currentResource = currentVersions?.find(
    (item) => item.version === version,
  );

  return {
    currentResource,
    currentVersions,
  };
}

export function useResourceSearch(
  data: z.infer<typeof listRegistry> | undefined,
) {
  const [searchQuery, setSearchQuery] = useState('');
  const searchQueryDebounced = useDebouncedValue(searchQuery, 150);

  const searched = useMemo(() => {
    if (!data || !searchQueryDebounced) return data;

    return data.filter((item) => {
      const itemWords = [item.namespace, item.name, ...item.tags].map((word) =>
        word.toLowerCase().replace(/[^a-zA-Z0-9]/g, ''),
      );
      const queryWords = searchQueryDebounced
        .split(' ')
        .map((word) => word.toLowerCase().replace(/[^a-zA-Z0-9]/g, ''));

      const matches = queryWords.every((queryWord) =>
        itemWords.find((itemWord) => itemWord.indexOf(queryWord) > -1),
      );

      return matches;
    });
  }, [data, searchQueryDebounced]);

  return {
    searched,
    searchQuery,
    setSearchQuery,
  };
}