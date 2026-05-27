import { Injectable } from '@nestjs/common';
import { PrismaService } from './prisma/prisma.service';

@Injectable()
export class AppService {
  constructor(private readonly prisma: PrismaService) {}

  async getHealth() {
    // eslint-disable-next-line @typescript-eslint/no-unsafe-call
    await this.prisma.$queryRaw`SELECT 1`;
    return { status: 'ok', service: 'API', database: 'connected' };
  }
}
